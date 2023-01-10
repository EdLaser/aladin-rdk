<script>
import axios from 'axios';
import { store } from './store';

export default {
    data() {
        return {
            generatedTasks: {},
            store
        }
    },
    methods: {
        getGeneratedTasks() {
            axios.get("http://localhost:8000/generated-tasks")
                .then((res) => {
                    console.log(res)
                    this.generatedTasks = res.data
                }).catch((error) => {
                    store.error = error.data
                });
        }
    },
    mounted() {
        this.getGeneratedTasks()
    }
}
</script>

<template>
    <ul class="list-group list-group-horizontal m-3">
        <template v-for="(solved, id) in generatedTasks">
            <a href="#" v-if="solved === true" class="list-group-item list-group-item-action list-group-item-success">Aufgabe: {{ id }}</a>
            <a href="#" v-else class="list-group-item list-group-item-action list-group-item-danger">Aufgabe: {{ id }}</a>
        </template>
    </ul>
</template>
