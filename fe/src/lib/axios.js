import axios from 'axios'

export const axiosClient = axios.create({
  baseURL: `${import.meta.env.VITE_API}/v1`,
})

axiosClient.interceptors.response.use(
  response => {
    return response.data;
  },
  error => {
    return Promise.reject(error);
  }
);

