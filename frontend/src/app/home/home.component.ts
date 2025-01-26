import {Component, inject} from '@angular/core';
import {CommonModule} from '@angular/common';
import {SensorService} from '../sensors.service';
import {SensorData} from "../sensordata";

@Component({
  selector: 'app-home',
  imports: [CommonModule],

  /**
   * HomeComponent displays the latest sensor data in a table.
   *
   * This component fetches sensor data from the SensorService when it is created.
   * The data is then displayed in a table and sorted by timestamp, with the most
   * recent data at the top.
   */

  template: `
    <section class="results">
      
      <h2>Latest Sensor Data</h2>
      
      <table>
        
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Temperature</th>
            <th>Humidity</th>
            <th>Vibration</th>
          </tr>
        </thead>
        
        <tbody>
          <tr *ngFor="let sensor of sensorDataList">
            <td>{{ sensor.timestamp }}</td>
            <td>{{ sensor.temperature }}°C</td>
            <td>{{ sensor.humidity }}%</td>
            <td>{{ sensor.vibration }}</td>
          </tr>
        </tbody>
      </table>
      
    </section>
  `,
  styleUrls: ['./home.component.css'],
})

export class HomeComponent {

  // List of sensor data
  sensorDataList: SensorData[] = [];

  // Inject the sensor service
  sensorService: SensorService = inject(SensorService);

  // When the component is created, get all sensor data
  constructor() {
    this.sensorService.getAllSensorData().then((sensorDataList: SensorData[]) => {
      this.sensorDataList = sensorDataList;
    });
  }
}





