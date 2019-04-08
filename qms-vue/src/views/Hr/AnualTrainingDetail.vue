<template>
  <div>
    <TabBlock/>
    <v-layout row wrap>
      <v-flex xs12>
          <anualList />
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import TabBlock from "../../components/Common/TabsBlock.vue";
import anualList from "../../components/AnualTraining/Detail.vue";

export default {
  components: {
    TabBlock,
    anualList
  }
};
</script>