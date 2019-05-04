<template>
  <div>
    <tabs/>
    <v-layout row wrap>
      <v-flex xs12>
        <Vlist/>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import Vlist from "../../components/Mr/InternalAuditReport.vue";
import tabs from "../../components/Common/TabsBlock.vue";
export default {
  name: "Feasibility",
  components: {
    Vlist,
    tabs
  },
};
</script>