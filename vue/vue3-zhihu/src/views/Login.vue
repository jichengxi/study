<template>
  <div class="login-page mx-auto p-3 w-330">
    <h5 class="my-4 text-center">登录到知乎</h5>
    <validate-from @form-submit="onFormSubmit">
      <div class="mb-3">
        <label class="form-label">邮箱地址</label>
        <validate-input
            :rules="emailRules" v-model="emailVal"
            placeholder="请输入邮箱地址"
            type="text"
            ref="inputRef"
        />
      </div>
      <div class="mb-3">
        <label class="form-label">密码</label>
        <validate-input
            :rules="passwordRules" v-model="passwordVal"
            placeholder="请输入密码"
            type="password"
        />
      </div>
      <template v-slot:submit>
        <span class="btn btn-danger">Submit</span>
      </template>
    </validate-from>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import ValidateInput, { RulesProp } from '@/components/ValidateInput.vue'
import ValidateFrom from '@/components/ValidateFrom.vue'

export default defineComponent({
  name: 'Login',
  components: { ValidateInput, ValidateFrom },
  setup () {
    const inputRef = ref<any>()
    const emailVal = ref('')
    const passwordVal = ref('')
    const emailRules: RulesProp = [
      { type: 'required', message: '电子邮箱不能为空' },
      { type: 'email', message: '请输入正确的电子邮箱格式' }
    ]
    const passwordRules: RulesProp = [
      { type: 'required', message: '密码不能为空' },
      { type: 'password', message: '请输入正确的密码格式' }
    ]
    const onFormSubmit = (result: boolean) => {
      console.log('result', result)
    }
    return {
      emailRules,
      passwordRules,
      emailVal,
      passwordVal,
      onFormSubmit,
      inputRef
    }
  }
})
</script>

<style>

</style>
