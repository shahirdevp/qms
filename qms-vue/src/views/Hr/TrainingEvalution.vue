<template>
  <div>
    <TabBlock/>
    <v-layout row wrap>
      <v-flex xs12>
          <evalution />
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import TabBlock from '../../components/Common/TabsBlock.vue';
import evalution from '../../components/TrainingEvalution/list.vue';

export default {
  components: {
    TabBlock,
    evalution
  }
};
</script>