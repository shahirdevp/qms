<template>
  <v-layout container>
    <v-flex xs12 sm6 md4>
      <v-card>
        <v-toolbar color="indigo lighten-1" dark v-if="!seen">
          <v-toolbar-title>Department</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon v-on:click="seen = !seen" v-if="!seen">
            <v-icon>add</v-icon>
          </v-btn>
        </v-toolbar>

        <v-toolbar color="indigo lighten-1" dark v-if="seen">
          <v-text-field
            v-model="todo"
            :append-outer-icon="'close'"
            @click:append-outer="seen = !seen"
            :append-icon="'send'"
            @click:append="savetodolist"
            class="ff"
          ></v-text-field>
          <template slot="append"></template>
        </v-toolbar>

        <v-list two-line>
          <template v-for="(item, index) in todos">
            <v-list-tile :key="item.title" avatar ripple>
              <v-list-tile-content>
                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
              </v-list-tile-content>

              <v-list-tile-action>
                <v-btn flat icon color="red" @click="deleteEvent(index)">
                  <v-icon>close</v-icon>
                </v-btn>
              </v-list-tile-action>
            </v-list-tile>
            <v-divider v-if="index + 1 < todos.length" :key="index"></v-divider>
          </template>
        </v-list>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import swal from "sweetalert2";
import router from "../../router";

export default {
  data() {
    return {
      show1: false,
      detail: [],
      todos: [{ title: "todo one" }, { title: "todo two" }],
      todo: "",
      seen: false,
      hide: true
    };
  },
  mounted() {},
  computed: {},
  methods: {
    savetodolist() {
      this.todos.push({ title: this.todo });
      this.todo = "";
    },

    deleteEvent(index) {
      this.todos.splice(index, 1);
    }
  }
};
</script>



<style scoped>
.two-column {
  column-count: 2;
  column-gap: 15px;
}
.three-column {
  column-count: 3;
  column-gap: 15px;
}
 .primary--text {
    color: #fff !important;
    caret-color: #fff !important;
}
</style>

<style>
.v-list--two-line .v-list__tile {
  height: 50px !important;
}
/*skill-matrix */
.depart-form {
  padding: 4px;
}
.lay-des {
  background: #fbfbfb;
  padding: 30px;
}
.skill-spac {
  line-height: 30px;
  padding: 0px;
  padding-left: 0px;
  padding-left: 15px;
}
.under-line {
  border-bottom: 1px dashed #bdbdbd;

  width: 100%;
}
.list-scroing {
  line-height: 30px;
  padding: 0px 0px 0px 14px;
}
.total-value p {
  float: right;
  margin-right: 52px;
  padding: 5px 25px;
  border-top: 1px solid;
  border-bottom: 1px solid;
}
.ap-list span {
  float: left;
  padding-right: 10px;
}
::before,
::after {
  text-decoration: inherit;
  vertical-align: inherit;
}
::selection {
  background-color: #b3d4fc;
  color: #000;
  text-shadow: none;
}
.ap-list {
  padding-top: 15px;
}
/* end skill-matrix */

.c-title {
  font-size: 20px;
  line-height: 35px;
  position: relative;
  margin-bottom: 20px;
}
.c-title:after {
  position: absolute;
  content: "";
  width: 100%;
  height: 1.5px;
  background-color: #e0e0e0;
  bottom: -5px;
  left: 0;
}
.c-list-lable {
  display: inline-block;
  width: 33%;
  color: #6f6f6f;
  padding: 0 5px 0 0px;
}
.c-list-content {
  display: inline-block;
  width: 67%;
  padding: 0 5px 0 0px;
}
.c-list {
  margin: 0 10px 25px 10px;
  padding: 10px 5px;
  width: calc(100% - 56px);
  position: relative;
}
.c-list::after {
  content: "";
  position: absolute;
  width: calc(100% - 65px);
  height: 1.5px;
  background: #dadada;
  left: 0;
  bottom: 0;
}
.c-list-lable::before {
  content: "";
  position: absolute;
  background: #77b8fb;
  height: 3px;
  width: 24%;
  bottom: -1px;
  left: 0px;
  z-index: 1;
}
.c-list-action {
  position: absolute;
  right: 4px;
  top: 0;
  width: 42px;
  opacity: 0;
  transition: 0.3s;
} /* .c-list:hover .c-list-action{opacity: 1;} */
.c-list-action .v-icon {
  font-size: 17px;
}
.c-right-date {
  display: inline-block;
  /* float: right; */
  position: absolute;
  right: 18px;
  top: 25px;
}
.dn {
  display: none;
}
.c-list-content-input input {
  width: calc(100% - 60px);
  border-bottom: 1px solid #fff0;
}
.c-list-content-input input:focus {
  border-bottom: 1px solid #77b8fb;
  box-shadow: 0px 5px 5px -7px #0042ff;
}
.block {
  display: block;
  width: 100%;
}
.form-box {
  width: calc(100% -65px);
  width: 90%;
} /*  input  */
.ic-list input,
.ic-list textarea,
.ic-list select {
  border: 1px solid #c6c6c6;
  width: calc(100% - 105px);
  padding: 8px 5px;
  margin-bottom: 15px;
  border-radius: 3px;
  margin-top: 3px;
}
.ic-list input:focus,
.ic-list textarea:focus,
.ic-list select:focus {
  border-color: #799df5;
  box-shadow: 0px 0px 3px #799df5;
}
.ic-list-lable {
  color: rgba(114, 114, 114, 1);
}
#empd .v-input__prepend-outer {
  display: none !important;
}
/* responsive */
@media (max-width: 768px) {
  .total-value p {
    float: right;
    margin-right: 0px;
  }
  .ap-list span {
    float: unset;
    padding-right: 0px;
    padding: 5px 10px;
  }
}
</style>





