<template>
  <div id="empd">
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Edit Stock Register</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right"></div>
      </v-flex>
    </v-layout>

    <!-- Insert-list-form -->
    <v-layout row class="lay-des1 white">
      <v-flex xs12 sm12 md11>
        <v-form ref="form" class v-model="valid" id="emp" lazy-validation>
          <v-layout class="white" row wrap>
           


             <v-flex md2>
              <label class="lab-for right black--text" > Part no </label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.part_no" outline type="text"></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text"> Description </label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-textarea
                  v-model="detail.description"
                  placeholder="Enter the value"
                  outline
                  rows="1"
                ></v-textarea>
              </div>
            </v-flex>
          

            <v-flex md2>
              <label class="lab-for right black--text">Doc ref </label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.doc_ref" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text"> Detail </label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-textarea
                  v-model="detail.detail"
                  placeholder="Enter the value"
                  outline
                  rows="1"
                ></v-textarea>
              </div>
            </v-flex>
         

            <v-flex md2>
              <label class="lab-for right black--text">Recipt </label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.recipt" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text"> Issue </label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-textarea
                  v-model="detail.issue"
                  placeholder="Enter the value"
                  outline
                  rows="1"
                ></v-textarea>
              </div>
            </v-flex>
          

            <v-flex md2>
              <label class="lab-for right black--text">Balance</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.balance" type="number" outline ></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Date</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.date" outline type="date"></v-text-field>
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
      auditArea: [],
      supplier:[]
    };
  },
  mounted() {
    this.getdetails();
    this.getSupplier();
  },
  methods: {
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        axios
          .put(this.$apiUrl + "pur/stock-register/" +  this.detail.id + '/', {
            part_no: this.detail.part_no,
            description: this.detail.description,
            doc_ref: this.detail.doc_ref,
            detail: this.detail.detail,
            recipt: this.detail.recipt,
            issue: this.detail.issue,
            balance: this.detail.balance,
            date: this.detail.date,
            owner: this.$owner
          })
          .then(function(response) {
            console.log(response.data);
            router.push("/stock-register/" + response.data.id);
          })
          .catch(function(error) {
            console.log(error);
          });
      }
    },

    getdetails() {
      var ts = window.location.pathname.split("/");
      var parQuery = ts[ts.length - 1];
      var self = this;
      axios
        .get(this.$apiUrl + "pur/stock-register/")
        .then(function(response) {
          self.detail = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    reset() {
      this.$refs.form.reset();
    }
  }
};
</script>


<style scoped>
.lab-for {
  line-height: 44px;
  margin-right: 8px;
}

</style>


