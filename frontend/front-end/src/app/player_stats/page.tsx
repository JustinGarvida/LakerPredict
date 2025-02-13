import PlayerStatsChart from "@/app/components/PlayerStatsChart";


export default function PlayerStatsPage() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Player Stats</h1>
      <p className="mb-6 text-gray-600">Visualizing player performance over the last 10 games.</p>
      <PlayerStatsChart />
    </div>
  );
}
