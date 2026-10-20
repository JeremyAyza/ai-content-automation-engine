from datetime import datetime

import pytest

import scripts.upload_youtube as upload
from pipeline.storage_csv import CsvStore


def freeze_now(monkeypatch, now: datetime):
    class FrozenDatetime(datetime):
        @classmethod
        def now(cls, tz=None):
            return now

    monkeypatch.setattr(upload, "datetime", FrozenDatetime)


def store_with_dates(tmp_path, dates):
    store = CsvStore(tmp_path / "ideas.csv")
    for i, date in enumerate(dates):
        idea = store.add_new_idea(f"Idea {i}", "mindset")
        idea.scheduled_date = date
        store.save(idea)
    return store


def test_first_video_goes_to_today_in_the_weekday_evening_slot(tmp_path, monkeypatch):
    freeze_now(monkeypatch, datetime(2026, 10, 19, 9, 0))  # Monday 09:00
    target = upload.get_next_schedule(store_with_dates(tmp_path, []))

    assert target.date() == datetime(2026, 10, 19).date()
    assert target.hour == 18 and 0 <= target.minute <= 45


def test_a_day_with_four_videos_moves_to_the_next_day(tmp_path, monkeypatch):
    freeze_now(monkeypatch, datetime(2026, 10, 19, 9, 0))
    store = store_with_dates(tmp_path, ["2026-10-20"] * 4)

    target = upload.get_next_schedule(store)

    assert target.date() == datetime(2026, 10, 21).date()


def test_keeps_filling_the_latest_scheduled_day(tmp_path, monkeypatch):
    freeze_now(monkeypatch, datetime(2026, 10, 19, 9, 0))
    store = store_with_dates(tmp_path, ["2026-10-20", "2026-10-22", "2026-10-22"])

    target = upload.get_next_schedule(store)

    assert target.date() == datetime(2026, 10, 22).date()


@pytest.mark.parametrize(
    "now, expected_day, hour_range",
    [
        (datetime(2026, 10, 24, 8, 0), 24, (10, 10)),  # Saturday: 10:00-10:30
        (datetime(2026, 10, 25, 8, 0), 25, (10, 11)),  # Sunday: 10:30-10:59
    ],
)
def test_weekend_slots_are_in_the_morning(tmp_path, monkeypatch, now, expected_day, hour_range):
    freeze_now(monkeypatch, now)
    target = upload.get_next_schedule(store_with_dates(tmp_path, []))

    assert target.day == expected_day
    assert hour_range[0] <= target.hour <= hour_range[1]


def test_never_schedules_less_than_an_hour_ahead(tmp_path, monkeypatch):
    freeze_now(monkeypatch, datetime(2026, 10, 19, 18, 30))  # Monday, past most of the slot
    target = upload.get_next_schedule(store_with_dates(tmp_path, []))

    assert target >= datetime(2026, 10, 19, 19, 30)


def test_youtube_date_format_is_spanish():
    assert upload.format_youtube_date(datetime(2026, 8, 28)) == "28 ago 2026"
    assert upload.format_youtube_time(datetime(2026, 8, 28, 9, 5)) == "09:05"
