'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;
process.stdin.on('data', function(inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on('end', function(): void {
    inputLines = inputString.split('\n');
    inputString = '';
    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}
function main() {
    function printArray<T>(arr: T[]): void {
        arr.forEach(function(element: T): void {
            console.log(element);
        });
    }

    const n: number = parseInt(readLine().trim(), 10);
    const intArray: number[] = [];
    for (let i = 0; i < n; i++) {
        intArray.push(parseInt(readLine().trim(), 10));
    }

    const m: number = parseInt(readLine().trim(), 10);
    const stringArray: string[] = [];
    for (let i = 0; i < m; i++) {
        stringArray.push(readLine().trim());
    }

    printArray<number>(intArray);
    printArray<string>(stringArray);
}