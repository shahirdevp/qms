<template>
  <div class>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
         <h3 class="page-name">Master List Of Internal & External Document</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <div :class="{dn : !dn}">
            <v-tooltip v-model="show" bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click.stop="dn = !dn">
                  <v-icon color="info">edit</v-icon>
                </v-btn>
              </template>
              <span>Edit</span>
            </v-tooltip>
            <v-tooltip v-model="show" bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click="deleteData()">
                  <v-icon color="red">delete</v-icon>
                </v-btn>
              </template>
              <span>Delete</span>
            </v-tooltip>
          </div>
          <div :class="{dn : dn}">
            <v-tooltip v-model="show" bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click.stop="dn = !dn">
                  <v-icon color="warning">close</v-icon>
                </v-btn>
              </template>
              <span>Cancel</span>
            </v-tooltip>
            <v-tooltip v-model="show" bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click="validate()">
                  <v-icon color="success">check</v-icon>
                </v-btn>
              </template>
              <span>Save</span>
            </v-tooltip>
          </div>
        </div>
      </v-flex>
    </v-layout>
    <!-- detail -->
    <v-layout container>
      <v-flex xs12 sm12 md10 offset-md1>
        <v-card>
          <v-layout class="lay-des-pad grey lighten-3" row wrap>
            <v-flex xs12>
              <h3 class="head black--text">Master List Of Internal & External Document</h3>
            </v-flex>
          </v-layout>
          <!-- <div class="under-line"></div> -->
          <!-- first list -->
          <v-layout class="lay-des1 white" row wrap>
            <v-flex md6 xs12 sm6>
              <p>
                <strong>SINO :</strong> 1
              </p>
              <p>
                <strong>Date :</strong> 2-4-2019
              </p>
              <p>
                <strong>Document Nmae:</strong> Text Dummy
              </p>
            </v-flex>
            <v-flex md6 xs12 sm6>
              <p>
                <strong>Type of Document:</strong> Type1
              </p>
              <p>
                <strong>Rev No :</strong> 5
              </p>
              <p>
                <strong>Doc Status :</strong> 435343
              </p>
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
      detail: [],
      dn: true,
      //  push to database
      valid: true,
      // languages

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
    },

    getdetails() {
      var ts = window.location.pathname.split("/");
      var parQuery = ts[ts.length - 1];
      var self = this;
      axios
        .get("http://127.0.0.1:8000/api/v1/hr/completency/" + parQuery)
        .then(function(response) {
          self.detail = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    validate: function() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        var self = this;

        var ts = window.location.pathname.split("/");
        var parQuery = ts[ts.length - 1];
        var self = this;

        axios({
          method: "put",
          url: "http://127.0.0.1:8000/api/v1/hr/completency/" + parQuery,
          data: {
            position: self.detail.position,
            education_Background: self.detail.education_Background,
            experience: self.detail.experience,
            competency_Requirement: self.detail.competency_Requirement
          }
        })
          .then(function(response) {
            self.dn = !response.dn;
            swal({
              title: "Success",
              type: "success",
              text: "Successfully edited",
              showConfirmButton: false,
              showCloseButton: false,
              timer: 3000
            });
          })
          .catch(function(error) {
            console.log(error);
          });
      }
    },
    deleteData() {
      var ts = window.location.pathname.split("/");
      var parQuery = ts[ts.length - 1];
      var self = this;
      swal({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
      }).then(result => {
        if (result.value) {
          axios
            .delete("http://127.0.0.1:8000/api/v1/hr/completency/" + parQuery)
            .then(function(response) {
              swal({
                title: "Success",
                text: "Successfully Delete",
                type: "success",
                showConfirmButton: false,
                showCloseButton: false,
                timer: 3000
              });
              router.push("/compentency-matrix");
            })
            .catch(function(error) {
              swal({
                type: "error",
                title: "Oops...",
                text: "Something went wrong!",
                showConfirmButton: false,
                showCloseButton: false,
                timer: 3000
              });
            });
        }
      });
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






