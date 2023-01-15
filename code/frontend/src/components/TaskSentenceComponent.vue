<script>
import { store } from './store';

export default {
    computed: {
        sentences() {
            return store.sentences;
        }
    },
    watch: {
        sentences() {
        }
    },
}
</script>
<template>
    <div class="container">
        <p>
            <template v-for="sentence in sentences">
                {{ sentence }}{{ " " }}
            </template>
        </p>
    </div>
</template>