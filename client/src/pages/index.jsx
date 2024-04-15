import Head from 'next/head'

export default function Home() {
  return (
    <div className='container'>
      <Head>
        <title>Product Review and Feedback System</title>
        <link rel="icon" href="/favicon.ico" />
        <link rel="stylesheet" href="/styles.css"/>
      </Head>

      <h1>Feedback App</h1>
    </div>
  )
}