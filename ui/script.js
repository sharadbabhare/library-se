function generateReport() {
    const report = 
`BookID | Title | Author | Status
B1 | Python Programming | Guido van Rossum | Available
B2 | Java Programming | James Gosling | Borrowed`;

    document.getElementById("output").textContent = report;
}
