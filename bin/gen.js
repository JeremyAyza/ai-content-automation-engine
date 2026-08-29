#!/usr/bin/env node
const { spawnSync } = require('child_process');
const path = require('path');

const args = process.argv.slice(2);
if (args.length < 2) {
    console.log("❌ Uso incorrecto.");
    console.log("👉 Ejemplos:");
    console.log("   gen short new        (Genera un video nuevo)");
    console.log("   gen short new x3     (Genera 3 videos nuevos)");
    console.log("   gen short s1 x2      (Ejecuta el paso 1 dos veces)");
    console.log("   gen short up         (Sube un video pendiente)");
    console.log("   gen short up x5      (Sube 5 videos pendientes)");
    process.exit(1);
}

const format = args[0]; // short | long
const action = args[1]; // new | s1..s7 | up

// Tolerancia inteligente: unimos todos los argumentos extra por si ponen "x 5" separado
const extraArgs = args.slice(2).join('').toLowerCase(); 

let times = 1;
if (extraArgs) {
    if (extraArgs.startsWith('x')) {
        const num = parseInt(extraArgs.slice(1), 10);
        if (isNaN(num) || num <= 0) {
            console.error(`❌ Error: El multiplicador está mal formateado. Escribiste '${args.slice(2).join(' ')}'. Debe ser un número, por ejemplo 'x5' o 'x 5'.`);
            process.exit(1);
        }
        times = num;
    } else {
        console.error(`❌ Error: Argumento desconocido '${args.slice(2).join(' ')}'. Si intentabas repetir el comando, usa el formato 'x5'.`);
        process.exit(1);
    }
}

const projectRoot = path.resolve(__dirname, '..');

// Map de acciones a comandos de poetry
const getCommands = (act) => {
    if (act === 'up') {
        return [['run', 'python', 'scripts/upload_youtube.py']];
    }
    
    // Si es 'new', ejecuta step1 (que fuerza una idea nueva) y luego 'fixed' para completarla hasta el final sin bucle infinito
    if (act === 'new') {
        return [
            ['run', 'python', '-m', 'pipeline.main', format, 'step1'],
            ['run', 'python', '-m', 'pipeline.main', format, 'fixed']
        ];
    }
    
    // Map s1 -> step1
    const stepMap = { 
        s1: 'step1', s2: 'step2', s3: 'step3', 
        s4: 'step4', s5: 'step5', s6: 'step6', 
        s7: 'step7', fixed: 'fixed', all: 'all'
    };
    let step = stepMap[act] ? stepMap[act] : act;
    
    return [['run', 'python', '-m', 'pipeline.main', format, step]];
};

const cmdArgsList = getCommands(action);

console.log(`\n🚀 Ejecutando [${format.toUpperCase()}] - [${action}] (${times} vece/s)\n`);

for (let i = 1; i <= times; i++) {
    if (times > 1) {
        console.log(`\n▶️ --- ITERACIÓN ${i} DE ${times} ---`);
    }
    
    for (const cmdArgs of cmdArgsList) {
        const result = spawnSync('poetry', cmdArgs, {
            cwd: projectRoot,
            stdio: 'inherit',
            shell: true
        });
        
        if (result.error) {
            console.error("❌ Error al ejecutar poetry:", result.error);
            process.exit(1);
        }
        if (result.status !== 0) {
            console.error(`❌ El proceso falló con código ${result.status} en la iteración ${i}`);
            process.exit(result.status);
        }
    }
}

console.log(`\n✅ Tarea finalizada exitosamente.\n`);
process.exit(0);
