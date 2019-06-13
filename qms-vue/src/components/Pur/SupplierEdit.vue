<template>
  <div id="empd">
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Edit Suppliers</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right"></div>
      </v-flex>
    </v-layout>

    <!-- Insert-list-form -->
    <v-layout row class="lay-des1 card-box white">
      <v-flex xs12 sm12 md11>
        <v-form ref="form" class v-model="valid" id="emp" lazy-validation>
          <v-layout class="white" row wrap>
            <v-flex md2>
              <label class="lab-for right black--text">Supplier</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.supplier" required="" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Email</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.email" outline type="email"></v-text-field>
              </div>
            </v-flex>

             <v-flex md2>
              <label class="lab-for right black--text" >Phone</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.phone" outline type="number"></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Country</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.country" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">State</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.state" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">City</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.city" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Street</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.street" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Pin</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.pin" outline type="number"></v-text-field>
              </div>
            </v-flex>

            

            <v-flex md2>
              <label class="lab-for right black--text">Website</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field outline v-model="detail.website" placeholder="http://example.com" type="url"></v-text-field>
              </div>
            </v-flex>
          </v-layout>
          <v-flex md12 offset-md2>
            <v-btn :disabled="!valid" color="success" @click="validate">Save</v-btn>
            <v-btn color="error" @click="reset">cancel</v-btn>
          </v-flex>
        </v-form>
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
      valid: true,
      auditArea: []
    };
  },
  mounted() {
    this.getData()
  },
  methods: {
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        var ts = window.location.pathname.split("/");
        var parQuery = ts[ts.length - 1];
        var self = this;
        axios
          .put (this.$apiUrl + "pur/supplier/" + parQuery + '/', {
            supplier: this.detail.supplier,
            country: this.detail.country,
            state: this.detail.state,
            city: this.detail.city,
            street: this.detail.street,
            pin: this.detail.pin,
            phone: this.detail.phone,
            email: this.detail.email,
            website: this.detail.website,
            owner: this.$owner
          })
          .then(function(response) {
            console.log(response.data);
            router.push("/suppliers/" + response.data.id);
          })
          .catch(function(error) {
            console.log(error);
          });
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    getData(){
      var ts = window.location.pathname.split("/");
      var parQuery = ts[ts.length - 1];
      var self = this;
      axios
              .get(this.$apiUrl + "pur/supplier/" + parQuery + '/')
              .then(function(response) {
                self.detail = response.data;
                console.log(response.data)
              })
              .catch(function(error) {
                console.log(error.data);
              });
    },
    
  }
};
</script>


<style scoped>
.lab-for {
  line-height: 44px;
  margin-right: 8px;
}
input [type="number"] {
  padding: 0;
}
</style>
