<template>
    <footer class="d-flex flex-row my-4 justify-content-center border-top text-white-50">
        <form method="POST" enctype="multipart/form-data">
            <div class="row mb-3">
                <label for="configFile" class="form-label">Upload Configs</label>
                <div class="col">
                    <input class="form-control" type="file" id="configFile" name="file">
                </div>
                <div class="col">
                    <button class="btn btn-primary" type="submit">Hochladen</button>
                </div>
            </div>
        </form>
    </footer>
</template>