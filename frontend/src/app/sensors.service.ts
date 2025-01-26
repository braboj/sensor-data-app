import {Injectable} from '@angular/core';
import {SensorData} from './sensordata';

@Injectable({
  providedIn: 'root',
})

export class SensorService {
  /**
   * Fetches all sensor data from the API.
   *
   * @returns A promise that resolves to an array of SensorData objects.
   */

  // The URL of the sensor data API */
  readonly url = 'http://localhost:5000/api/sensors';

  async getAllSensorData(): Promise<SensorData[]> {
    const data = await fetch(this.url);
    return (await data.json()) ?? [];
  }
}