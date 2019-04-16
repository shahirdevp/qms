<template>
  <div>
    <v-layout container class="tree-view-part">
      <v-flex md3>
        <v-treeview :items="item"></v-treeview>
      </v-flex>
    </v-layout>
  </div>
</template>


<style >
.tree-view-part.container {
  padding: 10% 0px;
}
.tree-view-part .v-treeview-node__children {
  float: right;
  position: relative;
  top: -83px;
  left: 70px;
}
.tree-view-part .v-treeview-node--leaf {
  background: #efefef;
  padding: 5px 20px;
  margin-bottom: 5px;
  border-radius: 30px;
}
</style>

<script>
export default {
  data: () => ({
    item: [
      {
        id: 1,
        name: "Applications :",
        children: [
          { id: 2,
           name: "Dummy text replay",
           children:[
               {
                   id: 3,
               }        

           ]
           },
          { id: 3, name: "Dummy text replay" },
          { id: 4, name: "Dummy text replay" }
        ]
      },
      
    ]
  })
};
</script>