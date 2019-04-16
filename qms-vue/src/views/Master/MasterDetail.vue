<template>
  <div>
    <v-layout row wrap>
      <v-flex xs12>
        <skills/>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import skills from "../../components/Master/Detail.vue";
import tabs from "../../components/Common/TabsBlock.vue";
export default {
  name: "Master",
  components: {
    skills,
    tabs
  },
};
</script>