const sachverhaltOptions = JSON.parse('{{cases_and_sums | tojson}}');
console.log(sachverhaltOptions);

const { createApp } = Vue
createApp({
    el: '#multiRowForm',
    data() {
        return {
            options: sachverhaltOptions,
            rows: [
                { 'select': 1, 'id': 0 }
            ]
        };
    },
    methods: {
        addRow: function () {
            try {
                newId = this.rows[this.rows.length -1]["id"] + 1
            } catch {
                newId = 0
            }
            this.rows.push({ 'select': 1, 'id': newId});
        },
        deleteRow: function (row) {
            const filteredRow = this.rows.filter(element => element !== row);
            this.rows = filteredRow;
        }
    }
}).mount('#multiRowForm')