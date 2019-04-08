<template>
  <div>
    <tabs/>
    <v-layout row wrap>
      <v-flex xs12>
        <hrdetails/>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import tabs from "../../components/Common/TabsBlock.vue";
import hrdetails from "../../components/Employee/Detail.vue";

export default {
  name: "Hrdetails",
  components: {
    tabs,
    hrdetails
  },
  
};
</script>