"use client";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

// Define data type
type DataPoint = {
  date: string;
  stat: number;
};

// Sample data for the last 10 games
const data: DataPoint[] = [
  { date: "2024-02-01", stat: 15 },
  { date: "2024-02-02", stat: 25 },
  { date: "2024-02-03", stat: 20 },
  { date: "2024-02-04", stat: 30 },
  { date: "2024-02-05", stat: 10 },
  { date: "2024-02-06", stat: 22 },
  { date: "2024-02-07", stat: 27 },
  { date: "2024-02-08", stat: 18 },
  { date: "2024-02-09", stat: 35 },
  { date: "2024-02-10", stat: 5 },
];

// Function to calculate mean and standard deviation
const calculateStats = (data: DataPoint[]) => {
  const values = data.map((d) => d.stat);
  const mean = values.reduce((a, b) => a + b, 0) / values.length;
  const stdDev = Math.sqrt(
    values.map((v) => Math.pow(v - mean, 2)).reduce((a, b) => a + b, 0) / values.length
  );
  return { mean, stdDev };
};

const { mean, stdDev } = calculateStats(data);
const thresholdHigh = mean + stdDev;
const thresholdLow = mean - stdDev;

// Define correct type for CustomBarShape
interface CustomBarProps {
  x?: number;
  y?: number;
  width?: number;
  height?: number;
  payload?: { stat: number };
}

// Custom bar shape function
const CustomBarShape: React.FC<CustomBarProps> = (props) => {
  const { x = 0, y = 0, width = 0, height = 0, payload } = props;
  let color = "#808080"; // Default grey

  if (payload && payload.stat !== undefined && payload.stat > thresholdHigh) color = "#00C851"; // Green for high outlier
  else if (payload && payload.stat !== undefined && payload.stat < thresholdLow) color = "#ff4444"; // Red for low outlier

  return <rect x={x} y={y} width={width} height={height} fill={color} />;
};

const PlayerStatsChart = () => {
  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="stat" shape={<CustomBarShape />} />
      </BarChart>
    </ResponsiveContainer>
  );
};

export default PlayerStatsChart;
