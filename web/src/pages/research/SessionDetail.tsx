interface Props {
  sessionId: string;
}

export default function SessionDetail({ sessionId }: Props) {
  return <div style={{ padding: 12 }}>Detail for {sessionId}</div>;
}
