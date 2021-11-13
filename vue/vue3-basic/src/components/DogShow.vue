<template>
    <img alt="Dog images" :src="result && result.message">
</template>

<script lang="ts">
import axios from "axios";
import {defineComponent} from "vue";

export default defineComponent( {
  name: "DogShow",
  async setup() {
    const rawData = await axios.get('https://dog.ceo/api/breeds/image/random')
    console.log(rawData.data)
    return {
      result: rawData.data
    }
  }
})
</script>

<style scoped>

</style>