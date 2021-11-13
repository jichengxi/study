import {reactive, toRefs, onMounted} from 'vue'
import axios from 'axios'

interface dataProps<T> {
    result: T|null;
    loading: boolean;
    loaded: boolean;
    error?: string;
}


function useURLLoader<T>(url: string) {
    // const result = ref(null)
    // const loading = ref(true)
    // const loaded = ref(false)
    // const error = ref(null)
    //
    // axios.get(url).then((data) => {
    //     loading.value = false
    //     loaded.value = true
    //     result.value = data.data
    // }).catch((err) => {
    //     error.value = err
    //     loading.value = false
    // })
    const data: dataProps<T|null> = reactive({
        result: null,
        loading: true,
        loaded: false,
        error: ''
    })
    onMounted(() => {
        axios.get(url).then((resData) => {
            data.loading = false
            data.loaded = true
            data.result = resData.data
            // console.log(url)
        }).catch((err) => {
            data.error = err
            data.loading = false
            // console.log(err)
        })
    })
    const refData = toRefs(data)
    return {...refData}
}

export default useURLLoader
