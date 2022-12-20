<script>
import TaskSentenceComponent from './TaskSentenceComponent.vue';

export default {
    components: {
        TaskSentenceComponent
    }
}
</script>
<template>
    <h1>Generierung einer Aufgabe</h1>
    <p class="lead">
        Hier werden Aufgaben zum Steuerrecht generiert!
    </p>
    <div class="container w-100 mb-5">
        <div class="row justify-content-center">
            <div class="col">
                <TaskSentenceComponent />
            </div>
            <div class="col">
                <!-- Costumize placholder -->
            </div>
        </div>
    </div>
    <div class="container">
        <div class="d-flex flex-row bd-highlight mb-3">
            <!-- Solution table placholder -->
        </div>
    </div>
</template>