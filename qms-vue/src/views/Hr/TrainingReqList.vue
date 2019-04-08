<template>
  <div>
    <tabs />
    <v-layout row wrap>
      <v-flex xs12>
        <traing/>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import traing from "../../components/TrainingRequest/list.vue";
import tabs from "../../components/Common/TabsBlock.vue";
export default {
  name: "Hr",
  components: {
    traing,
    tabs
  },
};
</script>