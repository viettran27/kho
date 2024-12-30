<script setup>
  import { ref } from 'vue'
  import { insertInventory } from './api/inventory'
  import { useToast } from './components/ui/toast'
  import Toaster from './components/ui/toast/Toaster.vue'
  
  const barcodeData = ref([])
  const estimate = ref(null)
  const total = ref(0)
  
  const { toast } = useToast()

  const getcurrentTime = (date) => {
    const dd = String(date.getDate()).padStart(2, '0');
    const mm = String(date.getMonth() + 1).padStart(2, '0');
    const yyyy = date.getFullYear();
    const hh = String(date.getHours()).padStart(2, '0');
    const min = String(date.getMinutes()).padStart(2, '0');
    const ss = String(date.getSeconds()).padStart(2, '0');

    return `${dd}/${mm}/${yyyy} ${hh}:${min}:${ss}`;
  }

  const checkExist = (value) => {
    return barcodeData.value.some((item) => item.code === value)
  }

  const handleChangeBarcode = (e) => {
    const value = e.target.value.trim()
    
    if (!value) return
    
    e.target.value = ''
    if (checkExist(value)) return
    
    const row = {
      "code": value,
      "datetime": new Date()
    }

    barcodeData.value = [row, ...barcodeData.value]
    total.value = barcodeData.value.length
  }

  const handleSave = async () => {
    const {type, message} = await insertInventory(barcodeData.value)
    toast({
      title: '',
      description: message,
      variant: type === 'success' ? 'success' : 'destructive'
    })
  }
</script>

<template>
  <div class="container flex flex-col py-2 relative h-[100vh] overflow-hidden">
    <div class="flex justify-center">
      <app-button class="w-full" @click="barcodeData = []; total = 0; estimate = null">Kiểm tra mới</app-button>
    </div>
    <div class="flex gap-2 mt-2 items-center">
      <div>Số lượng ước tính</div>
      <app-input 
        v-model="estimate"
        class="flex-1"
        placeholder="Nhập số lượng ước tính"
      />
    </div>
    <app-input 
      class="mt-2"
      placeholder="Đọc barcode ở đây"
      @input="handleChangeBarcode"
      @keydown.delete="e => e.target.value = ''"
    />
    <div><h1 class="my-2 text-center text-3xl font-bold">Tổng: {{ total }}</h1></div>
    <div class="overflow-auto">
      <app-table>
        <table-header class="sticky top-0 bg-white z-10">
          <table-row>
            <table-head class="w-1/2">Mã thùng</table-head>
            <table-head class="w-1/2">Thời gian thêm</table-head>
          </table-row>
        </table-header>
        <table-body>
          <table-row v-for="item in barcodeData" :key="item.code">
            <table-cell>{{ item.code }}</table-cell>
            <table-cell>{{ getcurrentTime(item.datetime) }}</table-cell>
          </table-row>
        </table-body>
      </app-table>
    </div>
    <div class="absolute bottom-0 py-4 bg-white z-10 w-[calc(100%-4rem)] flex justify-center">
      <app-button @click="handleSave" :disabled="!estimate || (Number(estimate) !== Number(total))" class="w-full">Lưu</app-button>
    </div>
  </div>
  <toaster />
</template>
