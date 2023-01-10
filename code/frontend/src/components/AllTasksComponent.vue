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
                    this.generatedTasks = res.data
                }).catch((error) => {
                    store.error = error.data
                });
        }
    },
    computed: {
        task_id() {
            return store.task_id
        }
    },
    watch: {
        task_id() {
            this.getGeneratedTasks()
        }
    }
}
</script>

<template>
    <div class="btn-group m-3" role="group" aria-label="Alle Aufgaben">
        <template v-for="(solved, id) in generatedTasks">
            <button v-if="solved === true" class="btn btn-success">Aufgabe: {{ id }}</button>
            <button v-else class="btn btn-danger">Aufgabe: {{ id }}</button>
        </template>
    </div>
</template>
