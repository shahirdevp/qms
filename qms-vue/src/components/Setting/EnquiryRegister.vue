<template>
  <div class>
    <v-layout row>
      <v-flex xs12 sm12 md12>
        <v-layout row wrap class="lay-out-res">
          <div class="lay-back">
            <v-flex md10>
              <h3 class="white--text">Enquiry Register</h3>
            </v-flex>
            <v-flex md2>
              <div class="lls">
                <v-btn icon color="white" class="bt-l">
                  <v-icon>edit</v-icon>
                </v-btn>
                <v-btn icon color="error" class="bt-l">
                  <v-icon>delete</v-icon>
                </v-btn>
              </div>
            </v-flex>
          </div>
        </v-layout>
      </v-flex>
    </v-layout>
    <!-- detail -->
    <v-layout container>
      <v-flex xs12 sm12 md12>
        <v-card>
          <v-layout row class="lay-des">
            <v-flex md3>
              <p><strong>SINO :</strong> 11-04-2019</p>
            </v-flex>
            <v-flex md3>
              <p><strong>Date :</strong> 11-04-2019</p>
            </v-flex>
            <v-flex md3>
              <p><strong>Customer :</strong> 11-04-2019</p>
            </v-flex>
            <v-flex md3>
              <p><strong>Contact :</strong> 11-04-2019</p>
            </v-flex>
          </v-layout>
          <v-layout row wrap>
            <v-flex md6>
              <div class="ees">
                <p><strong>Line no :</strong> 2</p>
                <p><strong>Part Namber :</strong> 6</p>
                <p><strong>Description :</strong> 6</p>
                <p><strong>Drawing Number :</strong> 11-04-2019</p>
                <p><strong>Qty :</strong> 11-04-2019</p>
              </div>
            </v-flex>
            <v-flex md6>
              <div class="ees">
                <p><strong>Quotation Ref :</strong> Dummy</p>
                <p><strong>Status :</strong> Nothing</p>
                <p><strong>Not In Scope :</strong> 7</p>
                <p><strong>Awarded :</strong> no awards</p>
                <p><strong>PO .NO :</strong> number</p>
              </div>
            </v-flex>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
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
/*skill-matrix */
.lay-des {
  background: #fbfbfb;
  padding: 20px 25px 0px 25px;
  border-bottom: 1px dashed gray;
}
.lay-out-res {
  background: #1976d2;
  padding: 25px;
}
.bt-l {
  margin: 0px 10px;
}

.ap-list span {
  float: left;
  padding-right: 10px;
}
.lay-back {
  width: 100%;
  padding: 0px;
  margin: 0px;
  display: inline-flex;
}

/* end skill-matrix */
</style>

<style>
.v-list--two-line .v-list__tile {
  height: 50px !important;
}
.ee {
  background: #f3f3f3;
  padding: 25px;
}
.ees {
  padding: 25px;
}

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





