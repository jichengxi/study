<template>
    <h1>{{result}}</h1>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
    name: "AsyncShow",
    setup() {
        return new Promise((resolve) => {
            setTimeout(() => {
                return resolve({
                    result: 42
                })
            }, 2000)
        })
    }
})
</script>

<style scoped>

</style>