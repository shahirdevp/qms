<template>
  <div>
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">HR REQUIRMENT REGISTER</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right">
          <v-btn color="primary" ref="fileInput" @click.stop="drawer = !drawer">
            Add Hr
            <v-icon right>add</v-icon>
          </v-btn>
        </div>
      </v-flex>
    </v-layout>

    <!-- Details -->
    <v-card style="margin:15px;padding:15px">
      <v-layout row wrap>
        <v-flex xs12>
          <div class="c-title">Basic Info</div>
        </v-flex>
        <v-flex xs6>
          <div class="c-ul">
            <div class="c-list">
              <div class="c-list-lable">EmployeeID</div>
              <div class="c-list-content">5INE-20171105-0056</div>
              <div class="c-list-action text-xs-center">
                <v-btn flat icon color="primary" small>
                  <v-icon>edit</v-icon>
                </v-btn>
              </div>
            </div>

            <div class="c-list">
              <div class="c-list-lable">EmployeeID</div>
              <div class="c-list-content">5INE-20171105-0056</div>
              <div class="c-list-action text-xs-center">
                <v-btn flat icon color="primary" small>
                  <v-icon>edit</v-icon>
                </v-btn>
              </div>
            </div>

            <div class="c-list">
              <div class="c-list-lable">EmployeeID</div>
              <div class="c-list-content">5INE-20171105-0056</div>
              <div class="c-list-action text-xs-center">
                <v-btn flat icon color="primary" small>
                  <v-icon>edit</v-icon>
                </v-btn>
              </div>
            </div>

            <div class="c-list">
              <div class="c-list-lable">EmployeeID</div>
              <div class="c-list-content">5INE-20171105-0056</div>
              <div class="c-list-action text-xs-center">
                <v-btn flat icon color="primary" small>
                  <v-icon>edit</v-icon>
                </v-btn>
              </div>
            </div>
          </div>
        </v-flex>

        <v-flex xs6>
          <div class="c-ul">
            <div class="c-list">
              <div class="c-list-lable">EmployeeID</div>
              <div class="c-list-content">5INE-20171105-0056</div>
              <div class="c-list-action text-xs-center">
                <v-btn flat icon color="primary" small>
                  <v-icon>edit</v-icon>
                </v-btn>
              </div>
            </div>

            <div class="c-list">
              <div class="c-list-lable">EmployeeID</div>
              <div class="c-list-content">5INE-20171105-0056</div>
              <div class="c-list-action text-xs-center">
                <v-btn flat icon color="primary" small>
                  <v-icon>edit</v-icon>
                </v-btn>
              </div>
            </div>

            <div class="c-list">
              <div class="c-list-lable">EmployeeID</div>
              <div class="c-list-content">5INE-20171105-0056</div>
              <div class="c-list-action text-xs-center">
                <v-btn flat icon color="primary" small>
                  <v-icon>edit</v-icon>
                </v-btn>
              </div>
            </div>

            <div class="c-list">
              <div class="c-list-lable">EmployeeID</div>
              <div class="c-list-content">5INE-20171105-0056</div>
              <div class="c-list-action text-xs-center">
                <v-btn flat icon color="primary" small>
                  <v-icon>edit</v-icon>
                </v-btn>
              </div>
            </div>
          </div>
        </v-flex>
      </v-layout>
    </v-card>
  </div>
</template>

<style scoped>
.two-column {
  column-count: 2;
  column-gap: 15px;
}
</style>

<style>
.c-title { font-size: 20px; line-height: 35px; position: relative; margin-bottom: 20px; }
.c-title:after { position: absolute; content: ""; width: 100%; height: 1.5px; background-color: #e0e0e0; bottom: -5px; left: 0; }
.c-list-lable { display: inline-block; width: 33%; color: #6f6f6f; }
.c-list-content { display: inline-block; width: 67%; }
.c-list { margin: 0 10px 25px 10px; padding: 10px 5px; width: calc(100% - 56px); position: relative; }
.c-list::after { content: ""; position: absolute; width: calc(100% - 65px); height: 1.5px; background: #dadada; left: 0; bottom: 0; }
.c-list-lable::before { content: ""; position: absolute; background: #77b8fb; height: 3px; width: 24%; bottom: -1px; left: 0px; z-index: 1; }
.c-list-action { position: absolute; right: 4px; top: 0; width: 42px; opacity: 0; transition:.3s; }
.c-list:hover .c-list-action{opacity: 1;}
.c-list-action .v-icon { font-size: 17px; }
</style>



<script>
export default {
  data() {
    return {};
  }
};
</script>