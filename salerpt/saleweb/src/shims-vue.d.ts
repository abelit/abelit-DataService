declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}

declare module "@vue/runtime-core" {
  import { AxiosInstance } from "axios";
  interface ComponentCustomProperties {
    $http: AxiosInstance;
  }
}