<template>
  <div>
    <v-layout row wrap>
      <v-flex xs12>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import skills from "../../components/Setting/Department.vue";
import tabs from "../../components/Common/TabsBlock.vue";
export default {
  name: "Setting",
  components: {
    skills,
    tabs
  },
};
</script>