<template>
  <div>
    <tabs />
    <v-layout row wrap>
      <v-flex xs12>
        <skills/>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import skills from "../../../components/SkillMatrix/Insert.vue";
import tabs from "../../../components/Common/TabsBlock.vue";
export default {
  name: "Hr",
  components: {
    skills,
    tabs
  },
};
</script>