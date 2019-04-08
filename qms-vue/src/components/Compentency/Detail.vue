<template>
  <div id="empd">
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Compentency Matrix</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <div :class="{dn : !dn}">
            <v-btn color="info" ref="fileInput" @click.stop="dn = !dn">
              Edit
              <v-icon right>edit</v-icon>
            </v-btn>
            <v-btn color="red" dark ref="fileInput" @click="deleteData()">
              Delete
              <v-icon right>delete</v-icon>
            </v-btn>
          </div>

          <div :class="{dn : dn}">
            <v-btn color="warning" ref="fileInput" @click.stop="dn = !dn">
              Cancel
              <v-icon right>close</v-icon>
            </v-btn>

            <v-btn color="success" ref="fileInput" @click="validate()">
              Save
              <v-icon right>check</v-icon>
            </v-btn>
          </div>
        </div>
      </v-flex>
    </v-layout>

    <!-- Details -->
    <v-card style="margin:15px;padding:15px" :class="{ dn: !dn }">
      <v-layout row wrap>
        <v-flex xs12>
          <div class="c-title">{{ detail.position }}</div>
          <div class="c-right-date">HR/F/01 Rev: 00 Date: {{ detail.created_On }}</div>
        </v-flex>
        <v-layout class="text-content" row wrap>
          <v-flex xs12 md6>
            <div class="c-ul">
              <div class="c-list">
                <div class="c-list-lable">Position</div>
                <div class="c-list-content">{{ detail.position }}</div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">Education Background</div>
                <div class="c-list-content">{{ detail.education_Background }}</div>
              </div>
              <div class="c-list">
                <div class="c-list-lable">Experience</div>
                <div class="c-list-content">{{ detail.experience }}</div>
              </div>

              <div class="c-list">
                <div class="c-list-lable">Competency Requirement</div>
                <div class="c-list-content">{{ detail.competency_Requirement }}</div>
              </div>
            </div>
          </v-flex>
        </v-layout>
      </v-layout>
    </v-card>

    <!-- Details -->
    <v-card style="margin:15px;padding:15px" :class="{ dn: dn }">
      <v-layout row wrap>
        <v-flex xs12>
          <div class="c-title">{{ detail.position }}</div>
          <div class="c-right-date">HR/F/01 Rev: 00 Date: {{ detail.created_On }}</div>
        </v-flex>
        <v-form ref="form" class="block" v-model="valid" lazy-validation>
          <v-layout class="text-content" row wrap>
            <v-flex xs12 md6>
              <div class="form-box">
                <v-text-field
                  v-model="detail.position"
                  :counter="50"
                  :rules="positionRules"
                  label="Position"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="detail.education_Background"
                  :counter="50"
                  :rules="eduBackgRules"
                  label="Education Background"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="detail.experience"
                  :counter="10"
                  type="number"
                  :rules="expRules"
                  label="Experience"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="detail.competency_Requirement"
                  :counter="50"
                  :rules="competencyRules"
                  label="Competency Requirement"
                  required
                ></v-text-field>
              </div>
            </v-flex>
          </v-layout>
        </v-form>
      </v-layout>
    </v-card>
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

      // form rules or validation
      positionRules: [v => !!v || "Employee Id is required"],
      eduBackgRules: [v => !!v || "Employee Id is required"],
      expRules: [v => !!v || "Employee Id is required"],
      competencyRules: [v => !!v || "Employee Id is required"]
    };
  },
  mounted() {
    this.getdetails();
  },
  computed: {},
  methods: {
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
</style>

<style>
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
  float: right;
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
</style>





