import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TareasComponent } from './tareas/tareas.component';
import { LoginComponent } from './login/login.component';
const routes: Routes = [     {path:'', component: LoginComponent},
  {path:'tareas/:id', component: TareasComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
