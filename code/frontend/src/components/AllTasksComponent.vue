<script>
import axios from 'axios';
import store from './store';

export default {
    data() {
        return {
            generatedTasks: {}
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
    }
}
</script>

<template>
    <ul class="list-group list-group-horizontal m-3">
        <template v-if="generatedTasks">
            <a href="#" class="list-group-item list-group-item-action">Aufgabe:Gelöst</a>
        </template>
    </ul>
</template>
