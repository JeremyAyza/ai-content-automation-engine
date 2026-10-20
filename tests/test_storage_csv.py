from pipeline.schemas import State
from pipeline.storage_csv import Column, CsvStore


def test_creates_the_csv_with_the_required_columns(tmp_path):
    csv_path = tmp_path / "out_short" / "ideas_tracking.csv"
    CsvStore(csv_path)

    header = csv_path.read_text().strip().split(",")
    assert header == [col.value for col in Column]


def test_new_ideas_get_consecutive_ids_and_start_as_new(tmp_path):
    store = CsvStore(tmp_path / "ideas.csv")

    first = store.add_new_idea("Compra la caída", "mindset")
    second = store.add_new_idea("La trampa del pago mínimo", "strategy")

    assert (first.id, second.id) == (1, 2)
    assert first.state == State.NEW
    assert store.get_next_id() == 3


def test_save_updates_state_and_scheduled_date(tmp_path):
    store = CsvStore(tmp_path / "ideas.csv")
    idea = store.add_new_idea("Idea", "mindset")

    idea.state = State.COMPLETED
    idea.scheduled_date = "2026-10-21"
    store.save(idea)

    saved = store.get_first_by_state(State.COMPLETED)
    assert saved is not None
    assert saved.id == idea.id
    assert saved.scheduled_date == "2026-10-21"
    assert store.get_first_by_state(State.NEW) is None


def test_incomplete_idea_skips_completed_and_uploaded(tmp_path):
    store = CsvStore(tmp_path / "ideas.csv")
    done = store.add_new_idea("Done", "mindset")
    uploaded = store.add_new_idea("Uploaded", "mindset")
    pending = store.add_new_idea("Pending", "mindset")

    done.state = State.COMPLETED
    uploaded.state = State.UPLOADED
    pending.state = State.AUDIO_GENERATED
    for idea in (done, uploaded, pending):
        store.save(idea)

    incomplete = store.get_incomplete_idea()
    assert incomplete is not None
    assert incomplete.title == "Pending"
    assert incomplete.state == State.AUDIO_GENERATED
