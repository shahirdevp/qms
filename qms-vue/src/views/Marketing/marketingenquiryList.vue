<template>
  <div>
    <tabs />
    <v-layout row wrap>
      <v-flex xs12>
        <vlist/>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import vlist from "../../components/Marketing/list.vue";
import tabs from "../../components/Common/TabsBlock.vue";
export default {
  name: "Hr",
  components: {
    vlist,
    tabs
  },
};
</script>
