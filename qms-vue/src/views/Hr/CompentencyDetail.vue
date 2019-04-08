<template>
  <div>
    <tabs/>
    <v-layout row wrap>
      <v-flex xs12>
        <compdetails/>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import tabs from "../../components/Common/TabsBlock.vue";
import compdetails from "../../components/Compentency/Detail.vue";

export default {
  name: "Hrdetails",
  components: {
    tabs,
    compdetails
  },
  
};
</script>