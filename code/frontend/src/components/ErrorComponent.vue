<script>
import { store } from './store';

export default {
    data() {
        return {
            store
        }
    },
    computed: {
        currentError() {
            return store.error
        }
    }
}
</script>
<template>
    <div class="row">
        {{ currentError }}
    </div>
</template>