#!/usr/bin/env node
const { spawnSync } = require('child_process');
const path = require('path');

const args = process.argv.slice(2);
let format = args[0];
let step = args[1] || 'all';

// Map s1 -> step1
const stepMap = { 
    s1: 'step1', s2: 'step2', s3: 'step3', 
    s4: 'step4', s5: 'step5', s6: 'step6', 
    s7: 'step7', fixed: 'fixed'
};

if (stepMap[step]) {
    step = stepMap[step];
}

if (!['short', 'long'].includes(format)) {
    console.log("❌ Uso incorrecto.");
    console.log("👉 Prueba con: generate short s1");
    console.log("👉 O también: generate long all");
    process.exit(1);
}

const projectRoot = path.resolve(__dirname, '..');
console.log(`\n🚀 Generando video [${format.toUpperCase()}] - paso: [${step}]`);

const result = spawnSync('poetry', ['run', 'python', '-m', 'pipeline.main', format, step], {
    cwd: projectRoot,
    stdio: 'inherit',
    shell: true
});

if (result.error) {
    console.error("Error al ejecutar poetry:", result.error);
    process.exit(1);
}

process.exit(result.status);
