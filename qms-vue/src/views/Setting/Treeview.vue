<template>
  <div>
    <v-layout row wrap>
      <v-flex xs12>
        <skills/>
         <TreeChart :json="data" :class="{landscape: landscape.length}" @click-node="clickNode" />
      </v-flex>
    </v-layout>
  </div>
</template>
<style>
  /* #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
#app .avat{border-radius: 2em;border-width:2px;}
#app .name{font-weight:700;}
.foot {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background: #333;
    padding: 24px;
    overflow: hidden;
    color: #999;
    font-size: 14px;
    text-align: center;
}
.foot a{color:#fff;margin:0 .5em}
</style>
<script>
import TreeChart from "../../components/Setting/Treeview.vue";
import tabs from "../../components/Common/TabsBlock.vue";
export default {
name: 'app',
  components: {
    TreeChart,
    tabs
  },
   data() {
    return {
      landscape: [],
      data: {
        name: 'root',
        image_url: "https://static.refined-x.com/avat.jpg",
        children: [
          {
            name: 'children1',
            image_url: "https://static.refined-x.com/avat1.jpg"
          },
          {
            name: 'children2',
            image_url: "https://static.refined-x.com/avat2.jpg",
            mate: {
              name: 'mate',
              image_url: "https://static.refined-x.com/avat3.jpg"
            },
            children: [
              {
                name: 'grandchild',
                image_url: "https://static.refined-x.com/avat.jpg"
              },
              {
                name: 'grandchild2',
                image_url: "https://static.refined-x.com/avat1.jpg"
              },
              {
                name: 'grandchild3',
                image_url: "https://static.refined-x.com/avat2.jpg"
              }
            ]
          }
        ]
      }
    }
  },
    methods: {
    toggleExtend: function(treeData){
      treeData.extend = !treeData.extend;
      this.$forceUpdate();
    }
  },
};
</script>