<template>
  <div class>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Supplier</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn-toggle class="transparent">
            <router-link :to="{ path: '../marketing-enquiry-edit/' + detail.id }" replace>
              <v-btn flat value="left">
                <span>Edit</span>
                <v-icon color="info">edit</v-icon>
              </v-btn>
            </router-link>
            <v-btn @click="deleteData()" flat value="center">
              <span>Delete</span>
              <v-icon color="red">delete</v-icon>
            </v-btn>
          </v-btn-toggle>
        </div>
      </v-flex>
    </v-layout>
    <!-- detail -->
    <v-layout>
      <v-flex xs12 sm12 md8  offset-md2>
          
            <v-card class="mt-3 ml-3 mr-3 custom-card-list">
                
                <v-card-text>
                    <div>
                        <h3 class=" mb-0">Supplier</h3>
                        <div>{{ detail.supplier }}</div>
                        <v-divider></v-divider>
                    </div>

                     <div>
                        <h3 class=" mb-0">Phone</h3>
                        <div>{{ detail.phone }}</div>
                        <v-divider></v-divider>
                    </div>

                    <div>
                        <h3 class=" mb-0">Email</h3>
                        <div>{{ detail.email }}</div>
                        <v-divider></v-divider>
                    </div>

                     <div>
                        <h3 class=" mb-0">Country</h3>
                        <div>{{ detail.country }}</div>
                        <v-divider></v-divider>
                    </div>

                    <div>
                        <h3 class=" mb-0">State</h3>
                        <div>{{ detail.state }}</div>
                        <v-divider></v-divider>
                    </div>

                     <div>
                        <h3 class=" mb-0">City</h3>
                        <div>{{ detail.city }}</div>
                        <v-divider></v-divider>
                    </div>

                    <div>
                        <h3 class=" mb-0">Street</h3>
                        <div>{{ detail.street }}</div>
                        <v-divider></v-divider>
                    </div>

                     <div>
                        <h3 class=" mb-0">Pin</h3>
                        <div>{{ detail.pin }}</div>
                        <v-divider></v-divider>
                    </div>

                    <div>
                        <h3 class=" mb-0">Website</h3>
                        <div>{{ detail.website }}</div>
                    </div>

                   
                </v-card-text>
                
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
      detail: []
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
        .get(this.$apiUrl + "pur/supplier/" + parQuery + '/')
        .then(function(response) {
          self.detail = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
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
            .delete(this.$apiUrl + "pur/supplier/" + parQuery + '/')
            .then(function(response) {
              swal({
                title: "Success",
                text: "Successfully Delete",
                type: "success",
                showConfirmButton: false,
                showCloseButton: false,
                timer: 3000
              });
              router.push("/suppliers");
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
.custom-card-list div { padding: 4px 0; }
.custom-card-list .v-card__text{ padding: 15px; }
.custom-card-list h3 { font-size: 16px; font-weight: 400; color:rgba(0,0,0,0.87); line-height: 24px}

</style>





