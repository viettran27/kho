import { axiosClient } from "@/lib/axios"

export const insertInventory = async (data) => {
  return axiosClient.post('/inventory', data)
}