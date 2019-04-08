<template>
  <div>
    <tabs />
    <v-layout row wrap>
      <v-flex xs12>
        <hrlist/>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import hrlist from "../../components/Hr/list.vue";
import tabs from "../../components/Common/TabsBlock.vue";
export default {
  name: "Hr",
  components: {
    hrlist,
    tabs
  },
};
</script>


