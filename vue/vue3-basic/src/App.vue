<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <h1>{{count}}</h1>
  <h1>{{double}}</h1>
  <ul>
    <li v-for="number in numbers" :key="number"><h3>{{number}}</h3></li>
  </ul>
  <h3>{{person.name}}</h3>
  <h1>{{greetings}}</h1>
  <p>{{err}}</p>
  <Suspense>
    <template #default>
      <div>
        <async-show />
        <dog-show />
      </div>
    </template>
    <template #fallback>
      <h1>loading ...</h1>
    </template>
  </Suspense>
  <model :is-open="modelIsOpen" @close-model="onModelClose">My Model !!</model>
  <button @click="openModel"> Open Model</button><br/>
  <h1 v-if="loading">Loading...</h1>
  <img alt="load image" v-if="loaded" :src="result[0].url">
  <h1>X: {{x}}, Y: {{y}}</h1>
  <button @click="increase">ｂ(￣▽￣)ｄ+1</button><br/>
  <button @click="updateGreeting">updateGreeting</button>

</template>

<script lang="ts">
import { defineComponent } from 'vue';
import HelloWorld from './components/HelloWorld.vue';
// onMounted, onUpdated, onRenderTriggered
import { ref, computed, reactive, toRefs, watch, onMounted, onUnmounted, onErrorCaptured } from 'vue';
import useMousePosition from '@/hooks/useMousePosition'
import useURLLoader from "@/hooks/useURLLoader";
import Model from "@/components/Model.vue";
import AsyncShow from "@/components/AsyncShow.vue";
import DogShow from "@/components/DogShow.vue";

interface DataProps {
  count: number;
  increase: () => void;
  double: number;
  numbers: number[];
  person: { name ?: string };
}

interface DogResult {
  message: string;
  status: string;
}

interface CatResult {
  id: string;
  url: string;
  width: number;
  height: number;
}

export default defineComponent({
  name: 'App',
  components: {Model, AsyncShow, DogShow},
  setup() {
    const err = ref(null)
    onErrorCaptured((error: any) => {
      err.value = error
      return true
    })
    // const count = ref(0)
    // const double = computed(() => {
    //   return count.value * 2
    // })
    // const increase = () => {
    //   count.value++
    // }
    // onMounted(() => {
    //   console.log('mounted')
    // })
    // onUpdated(() => {
    //   console.log('updated')
    // })
    // onRenderTriggered((event) => {
    //   console.log(event)
    // })
    const data: DataProps = reactive({
      count: 0,
      increase: () => {
        data.count++
      },
      double: computed(() => data.count * 2),
      numbers: [1, 2, 3],
      person: {}
    })
    const greetings = ref('')
    const updateGreeting = () => {
      greetings.value += 'Hello! '
    }

    // const {result, loading, loaded, error} = useURLLoader<DogResult>('https://dog.ceo/api/breeds/image/random')
    const {result, loading, loaded, error} = useURLLoader<CatResult[]>('http://api.thecatapi.com/v1/images/search?limit=1')
    watch (result, () => {
      if (result.value) {
        console.log('value', result.value[0].url)
      }
    })

    const { x, y } = useMousePosition()
    watch([greetings, () => data.count], (newValue, oldValue) => {
      console.log(oldValue)
      console.log(newValue)

      document.title = 'update' + greetings.value + data.count
    })
    data.numbers[0] = 5
    data.person.name = 'jcx'
    // return { count, increase, double }
    const refData = toRefs(data)

    const modelIsOpen = ref(false)
    const openModel = () => {
      modelIsOpen.value = true
    }
    const onModelClose = () => {
      modelIsOpen.value = false
    }

    return {...refData, greetings, updateGreeting, x, y, result, loading, loaded, modelIsOpen, openModel, onModelClose, err}
  }
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
