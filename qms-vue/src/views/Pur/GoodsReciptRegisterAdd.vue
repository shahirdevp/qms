<template>
  <div>
    <v-layout row wrap>
      <v-flex xs12>
        <tabs />
        <skills/>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import skills from "../../components/Pur/GoodsReciptRegisterAdd.vue";
import tabs from "../../components/Common/TabsBlock.vue";
export default {
  name: "PUD",
  components: {
    skills,
    tabs
  },
};
</script>