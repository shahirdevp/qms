<template>
  <div>
    <TabBlock></TabBlock>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Organization Chart</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn depressed  @click="saveTree"  value="left">
            <v-icon color="info" class="mr-1">save</v-icon>
            <span>Save</span>
          </v-btn>
        </div>
      </v-flex>
    </v-layout>
    <!-- <button @click="addNode">Add Node</button> -->
    <div class="tree-box card-box">
      <vue-tree-list
        @click="onClick"
        @change-name="onChangeName"
        @delete-node="onDel"
        @add-node="onAddNode"
        :model="data"
        default-tree-node-name="new node"
        default-leaf-node-name="new leaf"
        v-bind:default-expanded="false"
      >
        <span class="icon slot-icon" slot="addTreeNode">
          <v-icon color="teal ">create_new_folder</v-icon>
        </span>
        <span class="icon slot-icon" slot="addLeafNode">
          <v-icon color="orange ">add</v-icon>
        </span>
        <span class="icon slot-icon" slot="editNode">
          <v-icon color="info">edit</v-icon>
        </span>
        <span class="icon slot-icon" slot="delNode">
          <v-icon color="red">delete_outline</v-icon>
        </span>
      </vue-tree-list>
    </div>

    <div class="tree-box card-box">
      <button @click="getNewTree">Get new tree</button>
      <pre>
          {{newTree}}
      </pre>

      <div class="tf-tree example">
        <ul>
          <li>
            <span class="tf-nc">COE</span>
            <ul>
              <li>
                <span class="tf-nc">HR</span>
                <ul>
                  <li>
                    <span class="tf-nc">4</span>
                  </li>
                  <li>
                    <span class="tf-nc">5</span>
                    <ul>
                      <li>
                        <span class="tf-nc">9</span>
                      </li>
                      <li>
                        <span class="tf-nc">10</span>
                      </li>
                    </ul>
                  </li>
                  <li>
                    <span class="tf-nc">MR</span>
                  </li>
                  
                </ul>
              </li>
              <li>
                    <span class="tf-nc">MKT</span>
                  </li>
              <li>
                <span class="tf-nc">3</span>
                <ul>
                  <li>
                    <span class="tf-nc">7</span>
                  </li>
                  <li>
                    <span class="tf-nc">8</span>
                  </li>
                </ul>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { VueTreeList, Tree, TreeNode } from "vue-tree-list";
import TabBlock from "../../components/Common/TabsBlock.vue";
export default {
  components: {
    VueTreeList,
    TabBlock
  },
  data() {
    return {
      newTree: {},
      data: new Tree([
        {
          name: "CEO",
          id: 1,
          pid: 0,
          dragDisabled: true,
          addTreeNodeDisabled: false,
          addLeafNodeDisabled: true,
          editNodeDisabled: false,
          delNodeDisabled: true,
          children: []
        }
      ])
    };
  },
  mounted(){
    this.getchart();
  },

  methods: {
    //delete node
    onDel(node) {
      console.log(node);
      node.remove();
    },
    //update name
    onChangeName(params) {
      console.log(params);
    },
    //add node
    onAddNode(params) {
      console.log(params);
    },
    onClick(params) {
      console.log(params);
    },

    addNode() {
      var node = new TreeNode({name: "new node", isLeaf: false});
      if (!this.data.children) this.data.children = [];
      this.data.addChildren(node);
    },

    getNewTree() {
      var vm = this;

      function _dfs(oldNode) {
        var newNode = {};

        for (var k in oldNode) {
          if (k !== "children" && k !== "parent") {
            newNode[k] = oldNode[k];
          }
        }
        if (oldNode.children && oldNode.children.length > 0) {
          newNode.children = [];
          for (var i = 0, len = oldNode.children.length; i < len; i++) {
            newNode.children.push(_dfs(oldNode.children[i]));
          }
        }
        return newNode;
      }

      vm.newTree = _dfs(vm.data);
    },

    onClick(model) {
      console.log(model);
    },

    //  save to database
    saveTree() {
      this.getNewTree();
      axios.post(this.$apiUrl + "organization/org-process-chart", {
        chart: this.newTree
      }).then(function (response) {
        console.log(response)
      }).catch(function (error) {
        console.log(error);
      });
    },

  //  get data from api
    getchart(){
      var self = this;
      axios.get(this.$apiUrl + "organization/org-process-chart/3").then(function (response) {
        self.newTree = response.data.chart
      }).catch(function (error) {
        console.log(error);
      });
    }
  }
};
</script>


<style>
.vtl .vtl-drag-disabled {
  background-color: #d0cfcf;
}
.vtl .vtl-drag-disabled:hover {
  background-color: #d0cfcf;
}
.vtl .vtl-disabled {
  background-color: #d0cfcf;
}
</style>
<style  scoped>
.slot-icon i:hover {
  cursor: pointer;
  transform: scale(1.1);
  -webkit-transform: scale(1.3);
}
.slot-icon i {
  font-size: 15px;
  font-size: 16px;
  margin-right: 3px;
}
>>> .vtl-tree-node {
  padding: 10px 20px;
  width: 300px;
}
>>> .vtl-tree-node:hover {
  padding: 10px 20px;
}
.tree-box {
  overflow-x: auto;
}
.tes {
  padding: 20px;
  margin: 10px;
  background: red;
}

.tf-tree {
  font-size: 16px;
  overflow: auto;
}
.tf-tree * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
.tf-tree ul {
  display: inline-flex;
}
.tf-tree li {
  align-items: center;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  padding: 0 1em;
  position: relative;
}
.tf-tree li ul {
  margin: 2em 0;
}
.tf-tree li li:before {
  border-top: 0.0625em solid #000;
  content: "";
  display: block;
  height: 0.0625em;
  left: -0.03125em;
  position: absolute;
  top: -1.03125em;
  width: 100%;
}
.tf-tree li li:first-child:before {
  left: calc(50% - 0.03125em);
  max-width: calc(50% + 0.0625em);
}
.tf-tree li li:last-child:before {
  left: auto;
  max-width: calc(50% + 0.0625em);
  right: calc(50% - 0.03125em);
}
.tf-tree li li:only-child:before {
  display: none;
}
.tf-tree li li:only-child > .tf-nc:before,
.tf-tree li li:only-child > .tf-node-content:before {
  height: 1.0625em;
  top: -1.0625em;
}
.tf-tree .tf-nc,
.tf-tree .tf-node-content {
  border: 0.0625em solid #000;
  display: inline-block;
  padding: 0.5em 1em;
  position: relative;
}
.tf-tree .tf-nc:before,
.tf-tree .tf-node-content:before {
  top: -1.03125em;
}
.tf-tree .tf-nc:after,
.tf-tree .tf-nc:before,
.tf-tree .tf-node-content:after,
.tf-tree .tf-node-content:before {
  border-left: 0.0625em solid #000;
  content: "";
  display: block;
  height: 1em;
  left: calc(50% - 0.03125em);
  position: absolute;
  width: 0.0625em;
}
.tf-tree .tf-nc:after,
.tf-tree .tf-node-content:after {
  top: calc(100% + 0.03125em);
}
.tf-tree .tf-nc:only-child:after,
.tf-tree .tf-node-content:only-child:after,
.tf-tree > ul > li > .tf-nc:before,
.tf-tree > ul > li > .tf-node-content:before {
  display: none;
}
.tf-tree.tf-gap-sm li {
  padding: 0 0.6em;
}
.tf-tree.tf-gap-sm li > .tf-nc:before,
.tf-tree.tf-gap-sm li > .tf-node-content:before {
  height: 0.6em;
  top: -0.6em;
}
.tf-tree.tf-gap-sm li > .tf-nc:after,
.tf-tree.tf-gap-sm li > .tf-node-content:after {
  height: 0.6em;
}
.tf-tree.tf-gap-sm li ul {
  margin: 1.2em 0;
}
.tf-tree.tf-gap-sm li li:before {
  top: -0.63125em;
}
.tf-tree.tf-gap-sm li li:only-child > .tf-nc:before,
.tf-tree.tf-gap-sm li li:only-child > .tf-node-content:before {
  height: 0.6625em;
  top: -0.6625em;
}
.tf-tree.tf-gap-lg li {
  padding: 0 1.5em;
}
.tf-tree.tf-gap-lg li > .tf-nc:before,
.tf-tree.tf-gap-lg li > .tf-node-content:before {
  height: 1.5em;
  top: -1.5em;
}
.tf-tree.tf-gap-lg li > .tf-nc:after,
.tf-tree.tf-gap-lg li > .tf-node-content:after {
  height: 1.5em;
}
.tf-tree.tf-gap-lg li ul {
  margin: 3em 0;
}
.tf-tree.tf-gap-lg li li:before {
  top: -1.53125em;
}
.tf-tree.tf-gap-lg li li:only-child > .tf-nc:before,
.tf-tree.tf-gap-lg li li:only-child > .tf-node-content:before {
  height: 1.5625em;
  top: -1.5625em;
}
.tf-tree li.tf-dotted-children .tf-nc:after,
.tf-tree li.tf-dotted-children .tf-nc:before,
.tf-tree li.tf-dotted-children .tf-node-content:after,
.tf-tree li.tf-dotted-children .tf-node-content:before {
  border-left-style: dotted;
}
.tf-tree li.tf-dotted-children li:before {
  border-top-style: dotted;
}
.tf-tree li.tf-dotted-children > .tf-nc:before,
.tf-tree li.tf-dotted-children > .tf-node-content:before {
  border-left-style: solid;
}
.tf-tree li.tf-dashed-children .tf-nc:after,
.tf-tree li.tf-dashed-children .tf-nc:before,
.tf-tree li.tf-dashed-children .tf-node-content:after,
.tf-tree li.tf-dashed-children .tf-node-content:before {
  border-left-style: dashed;
}
.tf-tree li.tf-dashed-children li:before {
  border-top-style: dashed;
}
.tf-tree li.tf-dashed-children > .tf-nc:before,
.tf-tree li.tf-dashed-children > .tf-node-content:before {
  border-left-style: solid;
}
</style> 