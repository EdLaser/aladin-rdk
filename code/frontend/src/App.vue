<script>
import MainAppComponent from "./components/MainAppComponent.vue"

export default {
    components: {
        MainAppComponent
    }
}
</script>

<template>
    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
        <header class="mb-auto">
            <div>
                <h3 class="float-md-start mb-0">
                    Steuerrecht Aufgaben
                </h3>
                <nav class="nav nav-masthead justify-content-center float-md-end">
                    <a class="nav-link fw-bold py-1 px-0 active" href="https://github.com/EdLaser/aladin-rdk">
                        Aladin - Steuerrecht
                    </a>
                </nav>
            </div>
        </header>
        <main class="px-3">
            <MainAppComponent />
        </main>
    </div>
</template>
