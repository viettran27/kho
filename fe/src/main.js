import './assets/index.css'

import { createApp } from 'vue'
import App from './App.vue'
import Input from './components/ui/input/Input.vue'
import Button from './components/ui/button/Button.vue'
import Table from './components/ui/table/Table.vue'
import TableHeader from './components/ui/table/TableHeader.vue'
import TableRow from './components/ui/table/TableRow.vue'
import TableHead from './components/ui/table/TableHead.vue'
import TableCell from './components/ui/table/TableCell.vue'
import TableBody from './components/ui/table/TableBody.vue'

const app = createApp(App)
app.component('AppInput', Input)
app.component('AppButton', Button)
app.component('AppTable', Table)
app.component('TableHeader', TableHeader)
app.component('TableBody', TableBody)
app.component('TableRow', TableRow)
app.component('TableHead', TableHead)
app.component('TableCell', TableCell)


app.mount('#app')
